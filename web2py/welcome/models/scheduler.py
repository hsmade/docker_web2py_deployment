import logging
from datetime import datetime
from gluon.scheduler import Scheduler
from sessions2trash import single_loop
import gzip
import os

backup_path = '/backup'
backup_hours = 24
sessions_clean_hours = 16


def db_export(config, db=db):
    logger = logging.getLogger('db_export')

    if not os.access(backup_path, os.W_OK):
        message = 'Can\'t create files in: {0}'.format(backup_path)
        logger.error(message)
        raise IOError(message)
    backup_file = os.path.join(backup_path, 'database_export_{}.csv'.format(
        datetime.now().strftime('%Y%m%d-%H%M%S')
    ))
    logger.info('Writing backup to {0}'.format(backup_file))

    try:
        with gzip.open(backup_file, 'wb') as backup:
            db.export_to_csv_file(backup)
    except Exception as error:
        logger.exception(str(error))
        raise
    logger.info('Backup completed')
    return True


def delete_sessions():
    single_loop(auth.settings.expiration)


scheduler = Scheduler(db)

# schedule the backup
if not db((db.scheduler_task.task_name == 'db_export')).select():
    scheduler.queue_task(db_export,
                         pvars={},
                         timeout=60 * 10,
                         period=((60*60) * backup_hours),
                         repeats=0,
                         retry_failed=5)

# schedule the cleaning of the sessions
if not db((db.scheduler_task.task_name == 'delete_sessions')).select():
    scheduler.queue_task(delete_sessions,
                         pvars={},
                         timeout=60 * 10,
                         period=((60*60) * sessions_clean_hours),
                         repeats=0,
                         retry_failed=5)