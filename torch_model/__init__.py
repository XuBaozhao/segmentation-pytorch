from torch.optim import SGD, Adam, ASGD

from torch_model.blseg.model import PSPNet
from torch_model.net.DeepLabV3Plus.deeplab_v3plus import DeepLabV3Plus
from torch_model.net.FCN.fcn_4s import FCN
from torch_model.optimizer.radam import RAdam


def get_model(model_name, backbone, num_classes, in_c):
    assert model_name in ['DeepLabV3Plus', 'PSPNet', 'FCN']
    if model_name == 'DeepLabV3Plus':
        return DeepLabV3Plus(num_classes, in_channels=in_c, backbone=backbone, pretrained=True)
    if model_name == 'PSPNet':
        return PSPNet(backbone=backbone, num_classes=num_classes, in_c=in_c)
    if model_name == 'FCN':
        return FCN(num_classes, in_channels=in_c, backbone=backbone, pretrained=True)

    raise NotImplementedError


def get_optimizer(optim_name, parameters, lr):
    if optim_name == 'SGD':
        return SGD(parameters, lr, momentum=0.9, weight_decay=5e-4, nesterov=True)
    if optim_name == 'ASGD':
        return ASGD(parameters, lr, weight_decay=5e-4)
    if optim_name == 'Adam':
        return Adam(parameters, lr, weight_decay=5e-4)
    if optim_name == 'RAdam':
        return RAdam(parameters, lr, weight_decay=5e-4)
    raise NotImplementedError
