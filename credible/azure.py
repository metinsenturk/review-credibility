import datetime
from azure.storage.blob import BlockBlobService, PublicAccess
from azure.storage.blob import ContentSettings
from azure.storage.blob.sharedaccesssignature import BlobSharedAccessSignature


class Blob():
    def __init__(self, account_name, account_key, container_name):
        # blob service
        self.block_blob_service = BlockBlobService(
            account_name=account_name, account_key=account_key)
        self.blob_sas_service = BlobSharedAccessSignature(
            account_name, account_key)

        # init
        self.account_name = account_name
        self.account_key = account_key
        self.container_name = container_name
        self.create_container()

    def list_blobs(self):
        generator = self.block_blob_service.list_blobs(self.container_name)
        return list(generator)

    def create_container(self, container_name=None):
        to_be_deleted = ''
        if container_name is not None:
            to_be_deleted = container_name
        else:
            to_be_deleted = self.container_name

        status = self.block_blob_service.create_container(to_be_deleted)
        return status

    def delete_container(self):
        status = self.block_blob_service.delete_container(self.container_name)
        return status

    def delete_blob(self, blob_name):
        if self.block_blob_service.exists(self.container_name, blob_name):
            status = self.block_blob_service.delete_blob(
                self.container_name, blob_name)
        else:
            status = False
        return status

    def download_file(self, blob_name, full_path_to_file):
        blob = self.block_blob_service.get_blob_to_path(
            self.container_name, blob_name, full_path_to_file)
        return blob

    def upload_file(self, blob_name, full_path_to_file,
                    content_type='application/octet-stream', use_stream=True,
                    callback=None):
        content_setting = ContentSettings(content_type=content_type)

        if not use_stream:
            uploaded = self.block_blob_service.create_blob_from_path(
                self.container_name, blob_name, full_path_to_file,
                content_settings=content_setting, progress_callback=callback)
        else:
            uploaded = self.block_blob_service.create_blob_from_stream(
                self.container_name, blob_name, full_path_to_file,
                content_settings=content_setting, progress_callback=callback)
        return uploaded

    def generate_sas_for_container(self, days=1, **kwargs):
        start_time = datetime.datetime.now()
        expire_time = start_time + datetime.timedelta(days=days)

        token = self.blob_sas_service.generate_container(
            self.container_name, start=start_time,
            expiry=expire_time, **kwargs)
        return token


__doc__ = """
This module is a wrapper for azure blob service.

For more information about the azure python SDK, find information in here.
https://docs.microsoft.com/en-us/python/api/azure-storage-blob/azure.storage.blob.baseblobservice.baseblobservice?view=azure-python

More information on uploading file to blob is in here.
https://docs.microsoft.com/en-us/python/api/azure-storage-blob/azure.storage.blob.blockblobservice.blockblobservice?view=azure-python
"""
