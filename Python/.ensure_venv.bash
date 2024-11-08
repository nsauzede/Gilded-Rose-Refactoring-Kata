if [ "${BASH_SOURCE[0]}" -ef "$0" ] ; then
    echo "ERROR: you must source \"${BASH_SOURCE[0]}\", do not execute it"
    exit 1
fi

if [ $(python3 --version | cut -d ' ' -f 2 | cut -d '.' -f 2) -lt 12 ] ; then
  echo "ERROR: Python 3.8 or greater is required"
  return 1
fi

if [ -z "$VENV_DIR" ] ; then
  VENV_DIR=".venv"
fi

if [ ! -z "$VIRTUAL_ENV" ] ; then
  return 0
fi

if [ -f "$VENV_DIR/bin/activate" ] ; then
  . "$VENV_DIR/bin/activate"
  return 0
fi

\rm -rf "$VENV_DIR"
python3 -m venv "$VENV_DIR"
. "$VENV_DIR/bin/activate"
pip install --upgrade pip
pip install --requirement requirements.txt
