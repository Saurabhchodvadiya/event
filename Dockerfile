FROM python:3.10
RUN mkdir -p /F:\Company_test_Exam\event_management
# F:\Company_test_Exam\event_management
WORKDIR /F:\Company_test_Exam\event_management
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
COPY . .
EXPOSE 8000

# Run the Django development server
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]