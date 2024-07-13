# hng-devops-stage-3

## Project Description
This project integrates Flask with RabbitMQ, Celery, and SMTP to create a messaging system capable of sending emails asynchronously and logging events. It provides endpoints for sending emails and logging messages, which are queued using Celery for processing. The application is designed to be deployed behind Nginx for production environments, ensuring efficient routing and handling of requests.

## Introduction
Welcome to the Messaging System project! This application integrates Flask with RabbitMQ, Celery, and SMTP to enable asynchronous email sending and logging functionalities. It's designed to handle email tasks efficiently using Celery queues, ensuring robust performance and scalability. The project also includes configurations for deployment behind Nginx, making it suitable for production environments. Explore this README for setup instructions, usage guidelines, and more details on how to leverage this system effectively.

## Features
1. Asynchronous Email Sending: Utilizes Celery and RabbitMQ to queue and send emails asynchronously, enhancing performance and responsiveness.

2. Logging Functionality: Supports logging of activities to `/var/log/messaging_system.log`, providing a record of system interactions.

3. RESTful API Endpoint: Includes a Flask-based API endpoint (`/`) for handling parameters like `sendmail` for email sending and `talktome` for logging.

4. SMTP Configuration: Configures Flask-Mail to interact with an SMTP server for email delivery, supporting TLS encryption.

5. Deployment Readiness: Designed for deployment behind Nginx for production environments, ensuring robustness and security.


## Prerequisites
Ensure you have the following installed before proceeding:

- Python 3.6+
- RabbitMQ

## Installation

Clone the repository and install dependencies:

```bash
git clone https://github.com/your-username/your-repository.git
cd your-repository
pip install -r requirements.txt
```

## Usage

To run the project locally, follow these steps:

1. Configure Flask-Mail and Celery in `app.py`:
   
   ```python
   # Example configuration for Flask-Mail
   app.config.update(
       MAIL_SERVER='smtp.yourserver.com',
       MAIL_PORT=587,
       MAIL_USE_TLS=True,
       MAIL_USERNAME='your-email@example.com',
       MAIL_PASSWORD='your-email-password'
   )
   ```

2. Start RabbitMQ server:

   ```bash
   rabbitmq-server
   ```

3. Start the Flask application:

   ```bash
   python app.py
   ```

4. Access endpoints using a tool like ngrok for external testing:

   ```bash
   ngrok http 5000
   ```
