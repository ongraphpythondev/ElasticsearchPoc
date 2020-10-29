from django.shortcuts import render
from django.http import HttpResponse
from elasticsearch import Elasticsearch
es=Elasticsearch([{'host':'localhost','port':9200}])

def create_indices(request,index):
    es.indices.create(index=index, ignore=400)
    return HttpResponse("Successfully created")


def create_inges(request,_index):
    # index and doc_type you can customize by yourself
    data={"payload": {"test": True}}

    res = es.index(index=_index, doc_type='ingestion', body=data)
    # index will return insert info: like as created is True or False
    return HttpResponse("Successfully Created")
# Create your views here.
