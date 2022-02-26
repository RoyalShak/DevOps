FROM python
WORKDIR /RoyalShakFlask
RUN python --version
COPY requierments.txt .
RUN pip install --upgrade pip && pip install -r requierments.txt
COPY MainScores.py /RoyalShakFlask/MainScores.py
COPY Utils.py /RoyalShakFlask/Utils.py
COPY Scores.txt /RoyalShakFlask/Scores.txt
#CMD ["sh", "-c", "ls /RoyalShakFlask"]
CMD ["python", "-u", "MainScores.py"]
