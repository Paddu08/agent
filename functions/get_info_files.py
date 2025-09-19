import os 
def get_files_info(working_directory, directory=None):
 absolute_workDir=os.path.abspath(working_directory)
 if directory is None:
  directory='.'
 abs_directory=os.path.abspath(directory)
 if not abs_directory.startswith(absolute_workDir):
  return f'error "{directory}" is not a directory'
