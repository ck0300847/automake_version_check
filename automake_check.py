#encoding=utf8


import os

# For debug purpose
LOCAL_AUTOMAKE_VERSION_FILE = "local_automake_version.txt";
GPL_AUTOMAKE_VERSION_FILE = "aclocal.m4";

def get_local_automake_version():
  #local_host_automake_version = os.popen("automake --version").readline().rstrip("\n").split(" ")[3]


  # windows debug code
  local_host_automake_file = open(LOCAL_AUTOMAKE_VERSION_FILE, "r");
  #print(local_host_automake_string.readline())

  version = local_host_automake_file.readline().rstrip("\n").split(" ")[3];
  #print version;

  return version;

def get_gpl_automake_version():

  # if GPL_AUTOMAKE_VERSION_FILE does not exist, treat version is the same
  if os.path.isfile(GPL_AUTOMAKE_VERSION_FILE) == False:
    return 0;

  # windows debug code
  gpl_automake_file = open(GPL_AUTOMAKE_VERSION_FILE, "r");
  #print(local_host_automake_string.readline())

  version_array = gpl_automake_file.readline().rstrip("\n").split(" ");

  for i in range(len(version_array)):
    if version_array[i] == "aclocal" and ((i+1) < len(version_array)):
      return version_array[i+1];

  return 0;

def judge_main_and_subversion(localhost_version, gpl_version):

  localhost_subversion = localhost_version.split('.');
  gpl_subversion = gpl_version.split('.');
  if (localhost_subversion[0] == gpl_subversion[0]) \
    and (localhost_subversion[1] == gpl_subversion[1]):
    return 0;
  else:
    return 1;

def judge_automake_version(localhost_version, gpl_version):
  if judge_main_and_subversion(localhost_version, gpl_version) == 0:
    return 0;

  if localhost_version > gpl_version:
    return 1;
  elif localhost_version == gpl_version:
    return 0;
  else:
    return -1;


def Run():
  print('###########################');
  print('##     Start Run()       ##');
  print('###########################');

  # used to get the host automake version
  local_host_automake_version = get_local_automake_version();

  # check GPL automake version
  gpl_automake_version = get_gpl_automake_version();
  if gpl_automake_version == 0:
    return 0;

  # judge automake version is match
  print "local: " + local_host_automake_version;
  print "gpl: " + gpl_automake_version;
  return judge_automake_version(local_host_automake_version, gpl_automake_version);

if __name__ == '__main__':
  Ret = Run();
  print('###########################');
  print('##     Test Complete     ##');
  print('###########################');
  print Ret;