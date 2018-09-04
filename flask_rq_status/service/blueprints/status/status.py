"""Status Blueprint."""
from flask import Blueprint, render_template, url_for, redirect, flash
from flask_rq2 import RQ
from .manager import status_manager
import pandas as pd


status_handler = Blueprint(name='status',
                           import_name=__name__,
                           template_folder='templates',
                           static_folder='static')


@status_handler.route('/', methods=['GET'])
def index():
    """Render status page."""
    print('>>> status.index')
    return render_template('navigation_template.html',
                           page_title='flask-rq-status',
                           page_heading='Status Page',
                           url_for_back=url_for('landing.index'),
                           sub_pages=[
                               {'url': url_for('status.index'), 'label': "Status Page"},
                               {'url': url_for('status.job_create'), 'label': "Job Create"},
                               {'url': url_for('status.job_status'), 'label': "Job Status"},
                           ])


def expensive_job():
    import time
    time.sleep(10)


@status_handler.route('/job_create', methods=['GET'])
def job_create():
    """Job create."""
    job_queue = status_manager.get_queue()
    job = job_queue.enqueue(expensive_job)
    flash("Job Enqueued: {}".format(job.id))
    return redirect(url_for('status.index'))


@status_handler.route('/job_status', methods=['GET'])
def job_status():
    """Job status."""
    job_queue = status_manager.get_queue()
    for job_id in job_queue.job_ids:
        print(job_id)
        print(dir(job_id))
    return redirect(url_for('status.index'))
