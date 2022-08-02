""" 
This script demonstrates examples with configuring Looker Schedule Plans using Python SDK 

Example:
    Pause/Resume all schedules of a Look or a Dashboard: 
    	Usecase: Admins want to temporarily bulk-pausing all schedules when there are changes in ETL or LookML projects
    	that would lead to errors in sending schedules. Currently, there is no option in Looker UI to bulk-disable/enable schedules
    Copy all schedule settings of a Look (or a Dashboard) to another Look (or a Dashboard)
    	Usecase: Admins want to copy all schedule settings (destination plans, recipients, result options, etc.) of a Look or 
    	a Dashboard to another Look or Dashboard. Currently, there is no option in Looker UI to "copy" all schedules. 

Authors: Lan

Last modified: July 18, 2021
"""

import looker_sdk
from looker_sdk import models40
sdk = looker_sdk.init40(config_file='../looker.ini', section='Looker')


def get_schedules(id, content, user_id=None, all_users=True):

  """ Get all schedule plans of a Looker content owned by user_id
  
  Args: 
    id: id of the Looker content containing schedules    
    content(str): 'look', 'dashboard', or 'lookml_dashboard'
    user_id(int, optional): If user_id is None then return schedules owned by the user calling the API 
    all_users(bool, optional): If all_user is True then return schedules owned by all users 
  """

  if content == 'look':
    schedules = sdk.scheduled_plans_for_look(id, user_id=user_id, all_users=all_users)
  elif content == 'dashboard':
    schedules = sdk.scheduled_plans_for_dashboard(id, user_id=user_id, all_users=all_users)
  elif content == 'lookml_dashboard':
    schedules = sdk.schedule_plans_for_lookml_dashboard(id, user_id=user_id, all_users=all_users)
  return schedules
