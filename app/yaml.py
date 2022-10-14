import ruamel.yaml
import pathlib
from ruamel.yaml.scalarfloat import ScalarFloat
class WriteYaml:
  
  def __init__(self) -> None:
    """Constructor WriteYaml class
    """    
    #path info extraction
    self.path = str(pathlib.Path(__file__).parent.resolve())+'/'
    print(self.path)
    self.yaml = ruamel.yaml.YAML()
  
  def dict_to_yaml(self, file_name, dict_file):
    """Read the data from the form dictionary and save it in the corresponding .yml file

    Args:
        file_name (str): file path to write
        dict_file (python dic): form data request
    """    
    try:

      file_name_path = self.path+file_name
      with open(file_name_path) as fp:
        data_file = self.yaml.load(fp)

      for key in dict_file:
        if type(data_file[key]) == type(True):
          data_file[key] = bool(dict_file[key])
        elif type(data_file[key]) == type(12):
          data_file[key] = int(dict_file[key])
        elif type(data_file[key]) == ScalarFloat:
          data_file[key] = float(dict_file[key])
        else:
          data_file[key] = dict_file[key]

      with open(file_name_path, 'w') as fp:
        self.yaml.dump(data_file, fp)
    except (TypeError, FileNotFoundError) as e:
      return False, e.strerror
    return True, file_name
