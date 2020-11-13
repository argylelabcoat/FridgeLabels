import shlex
import shutil
import subprocess
import tempfile
import os

from datetime import datetime
from jinja2 import Template, FileSystemLoader, Environment

file_loader = FileSystemLoader('templates')
env = Environment(loader=file_loader)

template = env.get_template('datelabel.ms')

now = datetime.now()

output = template.render(year=now.year, month=now.month, day=now.day)

with tempfile.TemporaryDirectory() as temp_dir:
    labelfilepath = os.path.join(temp_dir, 'datelabel.ms')
    psfilepath = os.path.join(temp_dir, 'datelabel.ps')
    with open(labelfilepath, 'w') as outfile:
        outfile.write(output)
    cmd = "groff -ms -t -P -p1.25i,2.25i %s"%labelfilepath
    cmdparts = shlex.split(cmd)
    groff_output = subprocess.run(cmdparts, capture_output=True, text=True)
    with open(psfilepath, 'w') as outfile:
        outfile.write(groff_output.stdout)
    cmd = "lp -d Zebra_LP2824 %s"%psfilepath
    cmdparts = shlex.split(cmd)
    subprocess.run(cmdparts)
    
    

