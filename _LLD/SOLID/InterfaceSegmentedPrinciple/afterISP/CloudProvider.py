from abc import ABC,abstractmethod

# This is a interface for cloud hosting provider
class CloudHostingProvider(ABC):
    @abstractmethod
    def addServers():
        pass

    @abstractmethod
    def listServers():
        pass

   

# this interface for cloud storage provider
class CloudStorageProvider(ABC):
    @abstractmethod
    def uploadFile():
        pass

    @abstractmethod
    def getFile():
        pass

# this interface for cloud CDN provider
class CloudCDNProvider(ABC):
    @abstractmethod
    def getCDNAddresses():
        pass


# This AWS Server Provider class
class AWSProvider(CloudHostingProvider,CloudStorageProvider,CloudCDNProvider):
    def __init__(self) -> None:
        super().__init__()

    def addServers():
        print('Adding servers')

    def listServers():
        print('List of servers')

    def getCDNAddresses():
        print('this is CDN Address: xx.xx.xxx')

    def uploadFile():
        print('uploading a file')

    def getFile():
        print('getting a file')


# this is dropbox server provider
# this is voilating Interface segregation principle
class DropboxProvider(CloudStorageProvider):
    def __init__(self) -> None:
        super().__init__()

    def addServers():
        raise Exception('dropbox does not support this feature')
    
    def listServers():
        raise Exception('dropbox does not support this feature')

    def getCDNAddresses():
        raise Exception('dropbox does not support this feature')

    def uploadFile():
        print('uploading a file')

    def getFile():
        print('getting a file')