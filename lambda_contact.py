import json
import boto3
from botocore.exceptions import ClientError

ses = boto3.client('ses', region_name='us-east-1')

SYNCRO_EMAIL = 'ContactUs@yaliit.com'
FROM_ADDRESS = 'noreply@yaliit.com'

ALLOWED_ORIGINS = {'https://yaliit.com', 'https://www.yaliit.com'}


def lambda_handler(event, context):
    origin = event.get('headers', {}).get('origin', '')
    allow_origin = origin if origin in ALLOWED_ORIGINS else 'https://yaliit.com'

    cors_headers = {
        'Access-Control-Allow-Origin': allow_origin,
        'Access-Control-Allow-Headers': 'Content-Type',
        'Access-Control-Allow-Methods': 'POST,OPTIONS',
    }

    # Handle CORS preflight
    method = event.get('requestContext', {}).get('http', {}).get('method', '')
    if method == 'OPTIONS':
        return {'statusCode': 200, 'headers': cors_headers, 'body': ''}

    try:
        body = json.loads(event.get('body') or '{}')

        name     = body.get('name', '').strip()
        email    = body.get('email', '').strip()
        company  = body.get('company', '').strip()
        message  = body.get('message', '').strip()
        services = body.get('services', [])
        users    = body.get('users', '').strip()
        devices  = body.get('devices', '').strip()

        if not name or not email or not services:
            return {
                'statusCode': 400,
                'headers': cors_headers,
                'body': json.dumps({'error': 'Name, email, and at least one service are required.'})
            }

        # ── Build email subject ──
        subject = f"New Quote Request — {company or name}"

        # ── Build email body ──
        lines = []
        lines.append(f"New Quote Request — {company or name}")
        lines.append("=" * 45)
        lines.append("")

        lines.append("Services Requested:")
        for svc in services:
            lines.append(f"  ✓  {svc}")
        lines.append("")

        if users or devices:
            lines.append("Team Size:")
            if users:
                lines.append(f"  Users:    {users}")
            if devices:
                lines.append(f"  Devices:  {devices}")
            lines.append("")

        lines.append("Contact:")
        lines.append(f"  Name:     {name}")
        lines.append(f"  Email:    {email}")
        lines.append(f"  Company:  {company or 'N/A'}")
        lines.append("")

        if message:
            lines.append("Message:")
            lines.append(f"  {message}")

        body_text = "\n".join(lines)

        ses.send_email(
            Source=f'"{name}" <{FROM_ADDRESS}>',
            Destination={'ToAddresses': [SYNCRO_EMAIL]},
            Message={
                'Subject': {'Data': subject},
                'Body': {'Text': {'Data': body_text}},
            },
            ReplyToAddresses=[email],
        )

        return {
            'statusCode': 200,
            'headers': cors_headers,
            'body': json.dumps({'success': True})
        }

    except ClientError as e:
        print(f"SES error: {e}")
        return {
            'statusCode': 500,
            'headers': cors_headers,
            'body': json.dumps({'error': 'Failed to send message.'})
        }
