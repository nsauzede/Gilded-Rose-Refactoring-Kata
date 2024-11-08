#. .ensure_venv.bash
#complexipy gilded_rose.py
#exit 0

#uv init local/uv
#cd local/uv
#uv add complexipy
#uv venv
#uv run complexipy ../../gilded_rose.py
UVDIR=local/uv
WD=$PWD
UVOPT=-q
[ -d $UVDIR ] || uv init $UVOPT $UVDIR
cd $UVDIR
[ -d .venv ] || (uv venv $UVOPT ; uv add $UVOPT complexipy)
uv run $UVOPT complexipy $WD/g*.py
