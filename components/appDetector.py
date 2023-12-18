import subprocess

def is_program_installed(program):
   try:
       subprocess.run([program, "--version"], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
       return True
   except subprocess.CalledProcessError:
       return False