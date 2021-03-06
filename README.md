# Creating a DynamoDB using Python Scripts and AWS Cloud9

## Description

For this project, we are going to create a DynamoDB table within Amazaon AWS and populate it with data about sneakers using Python scripts. Everything is going to be done within an AWS Cloud9 environment. The code provided in this repository is for the two necessary Python scripts (one to create the database, the other to load the data), and a JSON file that contains the actual data.

This is a very simple table, but you can use the code as a basis for creating more elaborate or detailed DynamoDB tables

## Why?

There are many use cases for the creation of a DynamoDB table. DynamoDB is one of the core services of AWS and has a wide range of uses in applications. This project is a great way to get your feet wet and begin understanding how DynamoDB table creation works at a larger scale.

## Objectives

1. Create a Dynamodb table for my sneakers that has a partition key of the "Name of the brand" 
and sort key for the "Name of the sneaker model"
2. Use Python to create scripts for creating table and loading data
3. Do everything within an AWS Cloud9 Environment

## Prerequisites

1. AWS Account (everything done here will be on the free tier)
2. Python scripts and JSON data file (included in this repository)

# Instructions

1. Create a Cloud9 IDE from your AWS account
2. Upload files: `sneakertable.py loadsneakers.py sneakerdata.json` to the Cloud9 IDE
3. In Cloud9 terminal, run `python sneakertable.py` to create the table
4. run `python loadsneakers.py` to load the data
5. In your AWS console, navigate to DynamoDB, then select "tables" to ensure that the table has been created and properly populated

## Congratulations!

You just created a table in DynamoDB and popluated it using Python scripts and a JSON data file. Now, you can modify these files as necessary to suit your own needs, or run your own demos/tests.

