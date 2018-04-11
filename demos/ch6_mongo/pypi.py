import data.mongo_setup as setup
from data.package import Package
from bson import ObjectId


def main():
    setup.init_mongo()
    add_packages()
    show_packages()
    print("done.")


def show_packages():
    p = Package.objects(name="mongoengine").first()
    if not p:
        print("No package by that name")
        return

    print(f"Yay found: {p.name}")
    print("Maintainers: ")
    for m in p.maintainers:
        print(m)


def add_packages():
    if Package.objects().count() > 0:
        print("Already have data")
        return

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
