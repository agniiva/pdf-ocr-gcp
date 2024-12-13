# PDF OCR Service

A FastAPI-based microservice that extracts text from PDF documents using Optical Character Recognition (OCR) technology. The service can fetch PDFs from URLs, convert them to images, and extract text content using Tesseract OCR.

## Features

- PDF to text extraction via OCR
- URL-based PDF processing
- Bearer token authentication
- Docker containerization
- Cloud-ready deployment
- RESTful API interface

## Prerequisites

- Docker
- Python 3.10 or higher (for local development)
- Google Cloud Platform account (for cloud deployment)

## Local Development

1. Install dependencies:
```bash
pip install -r requirements.txt
```

2. Run the application:
```bash
python main.py
```

The service will be available at `http://localhost:8080`

## Docker Deployment

1. Build the Docker image:
```bash
docker build -t pdf-ocr-service .
```

2. Run the container:
```bash
docker run -p 8080:8080 -e AUTH_TOKEN=your_auth_token pdf-ocr-service
```

## API Usage

### Extract Text from PDF
```bash
curl -X POST http://localhost:8080/extract_text \
  -H "Authorization: Bearer test123" \
  -H "Content-Type: application/json" \
  -d '{"pdf_url": "https://example.com/sample.pdf"}'
```

### Response Format
```json
{
  "extracted_text": "Extracted content from the PDF..."
}
```

## Google Cloud Platform Deployment

### Prerequisites
1. Install Google Cloud SDK
2. Initialize gcloud and set your project:
```bash
gcloud init
gcloud config set project YOUR_PROJECT_ID
```

### Deploy to Cloud Run

1. Enable required APIs:
```bash
gcloud services enable run.googleapis.com
```

2. Build and push the container:
```bash
gcloud builds submit --tag gcr.io/YOUR_PROJECT_ID/pdf-ocr-service
```

3. Deploy to Cloud Run:
```bash
gcloud run deploy pdf-ocr-service \
  --image gcr.io/YOUR_PROJECT_ID/pdf-ocr-service \
  --platform managed \
  --region YOUR_REGION \
  --allow-unauthenticated \
  --set-env-vars="AUTH_TOKEN=your_secure_token"
```

### Environment Variables

- `PORT`: Server port (default: 8080)
- `AUTH_TOKEN`: Authentication token for API access

## Security Considerations

1. Always use a strong `AUTH_TOKEN` in production
2. Consider implementing rate limiting
3. Monitor API usage and implement appropriate quotas
4. Use HTTPS for all production endpoints
5. Regularly update dependencies for security patches

## Technical Architecture

The service follows a microservice architecture with the following components:

1. **FastAPI Application**: Handles HTTP requests and response formatting
2. **PDF Processing Pipeline**:
   - PDF fetching from URL
   - PDF to image conversion using pdf2image
   - OCR processing using Tesseract
3. **Authentication Layer**: Bearer token validation
4. **Error Handling**: Comprehensive error responses for various failure scenarios

## Performance Considerations

- Large PDFs may take longer to process
- Consider implementing async processing for large documents
- Memory usage scales with PDF size and complexity
- Implement appropriate timeouts for PDF downloads and processing

## Limitations

- Maximum PDF size is limited by available memory
- Processing time depends on PDF complexity and server resources
- Only text-based content can be extracted
- Image quality affects OCR accuracy

## Contributing

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Create a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details.
