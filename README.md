# VPC Flow Logs Monitoring with Grafana on AWS

This repository contains the source code and documentation for my final year project, which sets up a monitoring system for VPC Flow Logs using Grafana on AWS, with Telegram alerts for real-time notifications.

## Project Overview

The project builds a secure, scalable, and cost-effective VPC infrastructure on AWS, monitored via AWS CloudWatch and visualized with Grafana dashboards. Key features include:

- VPC Flow Logs setup for network traffic monitoring.
- Grafana dashboards for network traffic, resource utilization, and security events.
- Telegram bot integration for instant alerts.
- Infrastructure as Code (IaC) for consistent deployment.

## Repository Structure

- `iac/`: Infrastructure as Code files (e.g., CloudFormation templates for VPC and Flow Logs).
- `scripts/`: Bash scripts for automating EC2 and Grafana setup.
- `grafana/`: Grafana configuration files, including dashboards and data source provisioning.
- `telegram-bot/`: Python code for Telegram bot integration.

## Setup Instructions

1. **Deploy Infrastructure**  
   Use `iac/vpc-flow-logs.yaml` to create the VPC and enable Flow Logs via AWS CloudFormation.  
   Deploy in your AWS account using the AWS CLI or console.

2. **Set Up EC2 Instance**  
   Run `scripts/setup-ec2.sh` on an EC2 instance to install Docker and Grafana.  
   Ensure the instance has the IAM role `GrafanaCloudWatchRole` attached (see docs).

3. **Configure Grafana**  
   Copy `grafana/provisioning/datasources.yaml` to the Grafana provisioning directory.  
   Import dashboards from `grafana/dashboards/` (e.g., `vpc-network.json`).

4. **Set Up Telegram Bot**  
   Configure `telegram-bot/telegram-bot.py` with your Telegram bot token and channel ID.  
   Run the script on the EC2 instance or a Lambda function.

5. **Review Documentation**  
   See `docs/Final_Report.pdf` for detailed implementation details.  
   Follow `docs/Setup_Guide.md` for step-by-step setup instructions.

## Prerequisites

- AWS account with CLI configured.
- Docker installed on the EC2 instance.
- Python 3.x for the Telegram bot (if applicable).

## Notes for Reviewer

- Replace placeholder files (e.g., `vpc-flow-logs.yaml`, `telegram-bot.py`) with your actual implementations if they differ.  
- The final report in `docs/` provides comprehensive details on the project’s objectives, implementation, and results.
