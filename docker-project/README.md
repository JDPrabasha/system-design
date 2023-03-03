# Docker

You know how you have a toy box with different compartments for different toys? Well, imagine if you could have a magic toy box that can hold lots of different toys and each toy would be in its own separate box inside the big toy box.

That's what Docker does, but with computer programs instead of toys. Docker is a tool that lets you put different computer programs in their own separate boxes called "containers". Each container is like a little world where the program can run without interfering with other programs running on the same computer.

So, just like you can take a toy out of your toy box and play with it, you can take a program out of its container and use it on your computer. And if you don't want to play with that toy anymore, you can put it back in its box and take out a different toy. Similarly, if you don't need a program anymore, you can delete its container and use a different program instead.

That's basically what Docker does - it helps you keep different computer programs organized and separate so they don't get in each other's way.

## Notes

- RUN is an image build step, the state of the container after a RUN command will be committed to the container image. A Dockerfile can have many RUN steps that layer on top of one another to build the image. CMD is the command the container executes by default when you launch the built image.
- The docker-compose.yaml file can overide the CMD step in the Dockerfile, and can map local folders to folders in the container, s.t local changes are reflected in the container
