import data.mongo_setup as setup
from data.package import Package
from bson import ObjectId


def main():
    setup.init_mongo()
    add_packages()
    print("done.")


def add_packages():
    p = Package(name="mongoengine")
    p.maintainers.append(ObjectId())
    p.maintainers.append(ObjectId())
    p.maintainers.append(ObjectId())
    p.save()

    p = Package(name="requests")
    p.maintainers.append(ObjectId())
    p.maintainers.append(ObjectId())
    p.save()

    p = Package(name="jupyterlab")
    p.maintainers.append(ObjectId())
    p.save()


if __name__ == '__main__':
    main()
