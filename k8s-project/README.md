# Kubernetes

Let's say you create many cows (docker containers) with the same blueprint (docker image) and let the cows do their thing in the corral (docker daemon).

You have all the dairy cows in one place but it's getting pretty crowded and they're eating all the stuff around them (resources) and you need to redistribute them to other areas or they will die.

You hire the rancher named Kubernetes and tell him of all the other corrals (nodes). The rancher checks each corrals capacities (resources) that they can handle. The rancher will take care of moving the cows around when the corrals are low on food to more abundant areas and the rancher will also take care of creating new cows for you if cows die for any reason.

The rancher is responsible optimizing your cattle ranch as efficient as possible and making it scale as long as you tell him of all the locations that he's allowed to move the cows to. You can also tell him to only grow the ranch to a certain size or to dynamically scale larger to produce more milk based on the dairy consumption demand by the population (auto-scaling).

## Architecture

<img width="639" alt="image" src="https://user-images.githubusercontent.com/62155402/222864295-cdbd1c47-9837-474d-bc84-1fd0acdc8152.png">

## Notes

- <img width="1107" alt="image" src="https://user-images.githubusercontent.com/62155402/222864416-0a7e565c-9de8-4483-a648-2cc579184642.png">
- Run `kubectl apply -f <filename>.yaml` for each file in the kubernetes directory to start up the pods, service and ingress in that exact order
- Run `minikube tunnel`to access the ingress and observe how the load is balanced among the different pods

