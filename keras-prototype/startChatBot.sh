C='\033[0;31m'
NC='\033[0m'

echo  "${C}Is this the first time starting(y/n):${NC} "
read yesNoStart
echo  "${C}Do you want to Chat in the Angular Front End(y/n): ${NC}"
read yesNoFront
if [ "$yesNoStart" == 'y' ] || [ "$yesNoStart" == '' ]
then
  python3 -m pip install -r requirements.txt
  python3 model.py
  python3 -m spacy download de_core_news_sm

if [ "$yesNoFront" == 'y' ] || [ "$yesNoFront" == '' ]
then
  cd frontEnd
  npm install
  cd ..
fi
fi
if [ "$yesNoFront" == 'y' ] || [ "$yesNoFront" == '' ]
then
  trap "exit" INT TERM ERR
  trap "kill 0" EXIT

  python3 chatAPI.py&
  cd frontEnd
  ng serve&

  wait
else
  python3 chat.py
fi
