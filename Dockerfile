FROM python
COPY . /frontend
WORKDIR /frontend
EXPOSE 5000
RUN pip install -r requirements.txt
CMD ["python app.py"]