from operator import le
import ruamel.yaml
import pathlib
from ruamel.yaml.scalarfloat import ScalarFloat
class WriteYaml:
  
  def __init__(self) -> None:
    """Constructor WriteYaml class
    """    
    #path info extraction
    self.path = str(pathlib.Path(__file__).parent.resolve())+'/'
  
  def dict_to_yaml(self, file_name, dict_file, parents=None):
    """Read the data from the form dictionary and save it in the corresponding .yml file

    Args:
        file_name (str): file path to write
        dict_file (python dic): form data request
    """    
    dict_file = dict([(k, v) for k, v in dict_file.items() if len(v) > 0])
    yaml = ruamel.yaml.YAML()
    try:
      file_name_path = self.path+file_name
      with open(file_name_path) as fp:
        data_file = yaml.load(fp)
      print("######################################")
      print(data_file)
      if not parents == None:
        print("INCLUYE PARENTS")
        for parent in parents:
          data_aux = data_file['/**']['ros__parameters'][parent]

          print("######################################")
          print(file_name_path)
          print(data_aux)
          for key in dict_file:
            if type(data_aux[key]) == type(True):
              data_aux[key] = bool(dict_file[key])
            elif type(data_aux[key]) == type(12):
              data_aux[key] = int(dict_file[key])
            elif type(data_aux[key]) == ScalarFloat:
              data_aux[key] = float(dict_file[key])
            else:
              data_aux[key] = str(dict_file[key])
          data_file['/**']['ros__parameters'][parent] = data_aux
        with open(file_name_path, 'w') as fp:
          yaml.dump(data_file, fp)
      else:
        for key in dict_file:
          if type(data_file[key]) == type(True):
            data_file[key] = bool(dict_file[key])
          elif type(data_file[key]) == type(12):
            data_file[key] = int(dict_file[key])
          elif type(data_file[key]) == ScalarFloat:
            data_file[key] = float(dict_file[key])
          else:
            data_file[key] = str(dict_file[key])
        with open(file_name_path, 'w') as fp:
          yaml.dump(data_file, fp)
    except (TypeError, FileNotFoundError, KeyError) as e:
      print(e)
      return False, e.args
    return True, file_name
