# FDet-Offline: just like FDet, but offline

A version of [fdet](https://github.com/acnazarejr/fdet)
where you don't have to access the internet to download the weights.

These are the changes:

## MTCNN
### 1.

In fdet/mtcnn.py, line 73-76, the url for the MTCNN-weights are listed:

```python
base_url = 'https://github.com/acnazarejr/fdet/releases/download/weights/'
self._pnet = self.__load_model(_PNet, base_url + 'mtcnn_pnet.pt')
self._rnet = self.__load_model(_RNet, base_url + 'mtcnn_rnet.pt')
self._onet = self.__load_model(_ONet, base_url + 'mtcnn_onet.pt')
```
I downloaded those weights and put them in the directory ***weights***.
Then I changed the base_url to point to that directory.

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

## RetinaFace
### 1.

In fdet/retinaface.py, line 154-160:

```python
        
base_url = '../weights/'
if backbone == 'MOBILENET':
    url = 'mobilenet_v2-b0353104.pth'
else:
    url = 'resnet50-19c8e357.pth'
```