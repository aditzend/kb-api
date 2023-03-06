# 
FROM pytorch/pytorch:1.13.1-cuda11.6-cudnn8-runtime

# 
WORKDIR /code

# 
COPY ./app/requirements.txt /code/requirements.txt

# 
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

# 
COPY ./app /code/app

# 
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "80"]