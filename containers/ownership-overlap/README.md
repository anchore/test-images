# `ownership-overlap`
This is an image that has one package owned by another package. In this case an RPM (python-pil) that "owns" the installed python package "Pillow".

Syft should mark this relationship while engine should deduplicate these (preferring parent packages).