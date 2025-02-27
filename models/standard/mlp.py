"""
  默认模型
  简单三层神经网络[添加了Dropout层]
  本模型默认总参数量[参考基准：cifar10]：
    Total params:           394,634
    Trainable params:       394,634
    Non-trainable params:   0
"""

# pylint: disable=no-name-in-module
# pylint: disable=wildcard-import

from tensorflow.python.keras.models import Model
from hat.models.advance import AdvNet
from hat.models.network import NetWork


class mlp(NetWork, AdvNet):
  """
    MLP
  """
  
  def args(self):
    self.LOCAL_SIZE = 128
    self.DROP_RATE = 0.5

  def build_model(self):

    x_in = self.input(self.INPUT_SHAPE)

    x = self.flatten(x_in)
    x = self.local(x, self.LOCAL_SIZE)
    x = self.dropout(x, self.DROP_RATE)
    x = self.local(x, self.NUM_CLASSES, activation='softmax')

    self.model = Model(inputs=x_in, outputs=x, name='mlp')


# test part
if __name__ == "__main__":
  mod = mlp(DATAINFO={'INPUT_SHAPE': (32, 32, 3), 'NUM_CLASSES': 10})
  print(mod.INPUT_SHAPE)
  print(mod.model.summary())
