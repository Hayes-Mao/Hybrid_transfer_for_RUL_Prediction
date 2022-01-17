### Load Model ###
import torch.nn as nn
from torchvision import models
import torch

class transfer_model:
    
    def load_model(model_name):
        if model_name == 'resnet18':
            model = models.resnet18(pretrained=True)

        elif model_name == 'resnet50':
            model = models.resnet50(pretrained=True)

        elif model_name == 'resnet152':
            model = models.resnet152(pretrained=True)

        elif model_name == 'vgg11':
            model = models.vgg11(pretrained=True)

        elif model_name == 'googlenet':
            model = models.googlenet(pretrained=True)

        elif model_name == 'alexnet':
            model = models.alexnet(pretrained=True)

        elif model_name == 'efficientnet':
            model = models.efficientnet_b7(pretrained=True)
            
        elif model_name == 'densenet':
            model = models.densenet161(pretrained=True)
            
        elif model_name == 'regnet':
            model = models.regnet_y_32gf(pretrained=True)
            
        for param in model.parameters():
            param.requires_grad=False
            
        try:
            num_features = model.classifier[1].in_features
        except:
            pass
        
        try:
            num_features = model.fc.in_features
        except:
            pass
        
        try:
            num_features = model.classifier.in_features
        except:
            pass
            
        try:
            model.fc = nn.Sequential(
                    nn.Dropout(0.2),
                    nn.Linear(num_features, 512),
                    nn.ReLU(),
                    nn.Linear(512, 256),
                    nn.ReLU(),
                    nn.Linear(256, 1))
        except:
            model.classifier = nn.Sequential(
                    nn.Dropout(0.2),
                    nn.Linear(num_features, 512),
                    nn.ReLU(),
                    nn.Linear(512, 256),
                    nn.ReLU(),
                    nn.Linear(256, 1))
        
        if torch.cuda.is_available:
            model.cuda()
        return model

