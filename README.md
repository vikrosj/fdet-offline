# FDet-Offline: just like FDet, but offline

# NB Download like this: 
```console
pip install fdet-offline --find-links https://download.pytorch.org/whl/torch_stable.html
```

Package depends on torch-packages not in PyPi.

A version of [fdet](https://github.com/acnazarejr/fdet)
where you don't have to access the internet to download the weights.

These are the changes:

## MTCNN (only works for this model at the moment)
### 1.

In fdet/mtcnn.py, line 73-76, the url for the MTCNN-weights are listed:

```python
base_url = 'https://github.com/acnazarejr/fdet/releases/download/weights/'
self._pnet = self.__load_model(_PNet, base_url + 'mtcnn_pnet.pt')
self._rnet = self.__load_model(_RNet, base_url + 'mtcnn_rnet.pt')
self._onet = self.__load_model(_ONet, base_url + 'mtcnn_onet.pt')
```
I downloaded those weights and created packages to import them (because PyPi has a 100MB max on package size, this was the solution).

I put the weights in the directory **weights** in the package **fdet_offline_mtcnn_weights**.
The function **fdet_offline_mtcnn_weights.import_weights** takes *mtcnn_type* as input
and returns a partial function of [torch.load](https://pytorch.org/docs/stable/generated/torch.load.html#torch.load).

This partial function gets *map_location* from *__load_model*.

The previously mentioned fdet/mtcnn.py, line 73-76, now looks like this:

```python
self._pnet = self.__load_model(_PNet, 'pnet')
self._rnet = self.__load_model(_RNet, 'rnet')
self._onet = self.__load_model(_ONet, 'onet')
```

In fdet/mtcnn.py, what previously was (url was input):

```python

def __load_model(self, net_class: type, url: str) -> torch.nn.Module:
    """Download and construct the models"""
    try:
        state_dict = load_state_dict_from_url(url, map_location=self._device_control)
```

is now (mtcnn_type is input):


```python
def __load_model(self, net_class: type, mtcnn_type: str) -> torch.nn.Module:
    """Download and construct the models"""
    try:
        load_state_dict = import_weights.load_partial(mtcnn_type)
        state_dict = load_state_dict(map_location=self._device_control)
```


### 2.

At fdet/mtcnn.py, line 427:

```python
state_dict = load_state_dict_from_url(url, map_location=self._device_control)
```

[load_state_dict_from_url](https://pytorch.org/docs/stable/_modules/torch/hub.html#load_state_dict_from_url), returns a [torch.load](https://pytorch.org/docs/stable/generated/torch.load.html#torch.load) which takes the weight-file as input.
I replaced the load_state_dict_from_url with torch.load, and that's it. 

That line now states this instead;

```python
state_dict = torch.load(url, map_location=self._device_control)
```
