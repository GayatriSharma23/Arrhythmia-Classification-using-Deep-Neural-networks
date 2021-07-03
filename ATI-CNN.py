# -*- coding: utf-8 -*-
"""ATI-CNN

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1_astaOCMI1HyRGmMVbVui6_leQsp7y7w
"""

def my_model():
    nclass = 7
    input = Input(shape=(30000, 6))
    x = Convolution1D(16, kernel_size=5, activation='relu', padding="valid")(input)
    x = Convolution1D(16, kernel_size=5, activation='relu', padding="valid")(x)
    x = MaxPool1D(pool_size=2)(x)
    x = Dropout(0.2)(x)
  
    x = Convolution1D(32, kernel_size=3, activation='relu', padding="valid")(x)
    x = Convolution1D(32, kernel_size=3, activation='relu', padding="valid")(x)
    x = MaxPool1D(pool_size=2)(x)
    x = Dropout(0.2)(x)
    
    x = Convolution1D(32, kernel_size=3, activation='relu', padding="valid")(x)
    x = Convolution1D(32, kernel_size=3, activation='relu', padding="valid")(x)
    x = MaxPool1D(pool_size=2)(x)
    x = Dropout(0.2)(x)

    x = Convolution1D(64, kernel_size=3, activation='relu', padding="valid")(x)
    x = Convolution1D(64, kernel_size=3,activation='relu', padding="valid")(x)
    x = MaxPool1D(pool_size=2)(x)
    x = Dropout(0.2)(x)

    x = Convolution1D(128, kernel_size=3, activation='relu', padding="valid")(x)
    x = Convolution1D(128, kernel_size=3, activation='relu', padding="valid")(x)
    x = MaxPool1D(pool_size=2)(x)
    x = Dropout(0.2)(x)
   
    x = Convolution1D(256, kernel_size=3, activation='relu', padding="valid")(x)
    x = GlobalMaxPool1D()(x)
  

    
    dense_1 = Dense(nclass, activation='sigmoid', name='dense_3')(x)

    model = Model(inputs=input, outputs=dense_1)
    model.compile(loss ='binary_crossentropy', optimizer = Adam(0.001), metrics = ['accuracy'])
   
    return model