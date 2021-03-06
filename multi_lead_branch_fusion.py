# -*- coding: utf-8 -*-
"""Multi Lead Branch Fusion

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1RfMexPUadW9T6txCWITOdRUBhsP-DOE8
"""

input = Input(shape=(30000,6), dtype='float32', name= 'input')
x = Conv1D(12,kernel_size=3,strides=1, padding='same')(input)
x = LeakyReLU(alpha=0.3)(x)
x = Conv1D(12,kernel_size=3,strides=1, padding='same')(x)
x = LeakyReLU(alpha=0.3)(x)
x = Conv1D(12,kernel_size=24, strides = 2, padding='same')(x)
x = LeakyReLU(alpha=0.3)(x)
x = Dropout(0.2)(x)

x = Conv1D(12,kernel_size=3,strides=1, padding='same')(x)
x = LeakyReLU(alpha=0.3)(x)
x = Conv1D(12,kernel_size=3,strides=1, padding='same')(x)
x = LeakyReLU(alpha=0.3)(x)
x = Conv1D(12,kernel_size=24, strides = 2, padding='same')(x)
x = LeakyReLU(alpha=0.3)(x)
x = Dropout(0.2)(x)

x = Conv1D(12,kernel_size=3,strides=1, padding='same')(x)
x = LeakyReLU(alpha=0.3)(x)
x = Conv1D(12,kernel_size=3,strides=1, padding='same')(x)
x = LeakyReLU(alpha=0.3)(x)
x = Conv1D(12,kernel_size=24, strides = 2, padding='same')(x)
x = LeakyReLU(alpha=0.3)(x)
x = Dropout(0.2)(x) 

x = Conv1D(12,kernel_size=3,strides=1, padding='same')(x)
x = LeakyReLU(alpha=0.3)(x)
x = Conv1D(12,kernel_size=3,strides=1, padding='same')(x)
x = LeakyReLU(alpha=0.3)(x)
x = Conv1D(12,kernel_size=24, strides = 2, padding='same')(x)
x = LeakyReLU(alpha=0.3)(x)
x = Dropout(0.2)(x)

x = Conv1D(12,kernel_size=3,strides=1, padding='same')(x)
x = LeakyReLU(alpha=0.3)(x)
x = Conv1D(12,kernel_size=3,strides=1, padding='same')(x)
x = LeakyReLU(alpha=0.3)(x)
x = Conv1D(12,kernel_size=48, strides = 2, padding='same')(x)
x = LeakyReLU(alpha=0.3)(x)
x = Dropout(0.2)(x)
x1= Bidirectional(GRU(12, input_shape=(938,6),return_sequences=True,return_state=False),merge_mode='concat')(x)
x = LeakyReLU(alpha=0.3)(x1)
x = Dropout(0.2)(x)
x = AttentionWithContext()(x)
x = BatchNormalization()(x)
x = LeakyReLU(alpha=0.3)(x)
x = Dropout(0.2)(x)
x = Dense(7,activation='sigmoid')(x)

   

                                                                       #SECOND MODEL


x = Conv1D(12,kernel_size=3,strides=1, padding='same')(input)
x = LeakyReLU(alpha=0.3)(x)
x = Conv1D(12,kernel_size=3,strides=1, padding='same')(x)
x = LeakyReLU(alpha=0.3)(x)
x = Conv1D(12,kernel_size=24, strides = 2, padding='same')(x)
x = LeakyReLU(alpha=0.3)(x)
x = Dropout(0.2)(x)

x = Conv1D(12,kernel_size=3,strides=1, padding='same')(x)
x = LeakyReLU(alpha=0.3)(x)
x = Conv1D(12,kernel_size=3,strides=1, padding='same')(x)
x = LeakyReLU(alpha=0.3)(x)
x = Conv1D(12,kernel_size=24, strides = 2, padding='same')(x)
x = LeakyReLU(alpha=0.3)(x)
x = Dropout(0.5)(x)

x = Conv1D(12,kernel_size=3,strides=1, padding='same')(x)
x = LeakyReLU(alpha=0.3)(x)
x = Conv1D(12,kernel_size=3,strides=1, padding='same')(x)
x = LeakyReLU(alpha=0.3)(x)
x = Conv1D(12,kernel_size=24, strides = 2, padding='same')(x)
x = LeakyReLU(alpha=0.3)(x)
x = Dropout(0.2)(x) 

x = Conv1D(12,kernel_size=3,strides=1, padding='same')(x)
x = LeakyReLU(alpha=0.3)(x)
x = Conv1D(12,kernel_size=3,strides=1, padding='same')(x)
x = LeakyReLU(alpha=0.3)(x)
x = Conv1D(12,kernel_size=24, strides = 2, padding='same')(x)
x = LeakyReLU(alpha=0.3)(x)
x = Dropout(0.2)(x)


x = Conv1D(12,kernel_size=3,strides=1, padding='same')(x)
x = LeakyReLU(alpha=0.3)(x)
x = Conv1D(12,kernel_size=3,strides=1, padding='same')(x)
x = LeakyReLU(alpha=0.3)(x)
x = Conv1D(12,kernel_size=48, strides = 2, padding='same')(x)
x = LeakyReLU(alpha=0.3)(x)
x = Dropout(0.2)(x)
x2 = Bidirectional(GRU(12, input_shape=(938,6),return_sequences=True,return_state=False),merge_mode='concat')(x)
x = LeakyReLU(alpha=0.3)(x2)
x = Dropout(0.2)(x)
x = AttentionWithContext()(x)
x = BatchNormalization()(x)
x = LeakyReLU(alpha=0.3)(x)
x = Dropout(0.2)(x)
x = Dense(7,activation='sigmoid')(x)




                                                                          #THIRD MODEL


x = Conv1D(12,kernel_size=3,strides=1, padding='same')(input)
x = LeakyReLU(alpha=0.3)(x)
x = Conv1D(12,kernel_size=3,strides=1, padding='same')(x)
x = LeakyReLU(alpha=0.3)(x)
x = Conv1D(12,kernel_size=24, strides = 2, padding='same')(x)
x = LeakyReLU(alpha=0.3)(x)
x = Dropout(0.2)(x)

x = Conv1D(12,kernel_size=3,strides=1, padding='same')(x)
x = LeakyReLU(alpha=0.3)(x)
x = Conv1D(12,kernel_size=3,strides=1, padding='same')(x)
x = LeakyReLU(alpha=0.3)(x)
x = Conv1D(12,kernel_size=24, strides = 2, padding='same')(x)
x = LeakyReLU(alpha=0.3)(x)
x = Dropout(0.2)(x)

x = Conv1D(12,kernel_size=3,strides=1, padding='same')(x)
x = LeakyReLU(alpha=0.3)(x)
x = Conv1D(12,kernel_size=3,strides=1, padding='same')(x)
x = LeakyReLU(alpha=0.3)(x)
x = Conv1D(12,kernel_size=24, strides = 2, padding='same')(x)
x = LeakyReLU(alpha=0.3)(x)
x = Dropout(0.2)(x) 

x = Conv1D(12,kernel_size=3,strides=1, padding='same')(x)
x = LeakyReLU(alpha=0.3)(x)
x = Conv1D(12,kernel_size=3,strides=1, padding='same')(x)
x = LeakyReLU(alpha=0.3)(x)
x = Conv1D(12,kernel_size=24, strides = 2, padding='same')(x)
x = LeakyReLU(alpha=0.3)(x)
x = Dropout(0.2)(x)


x = Conv1D(12,kernel_size=3,strides=1, padding='same')(x)
x = LeakyReLU(alpha=0.3)(x)
x = Conv1D(12,kernel_size=3,strides=1, padding='same')(x)
x = LeakyReLU(alpha=0.3)(x)
x = Conv1D(12,kernel_size=48, strides = 2, padding='same')(x)
x = LeakyReLU(alpha=0.3)(x)
x= Dropout(0.2)(x)
x3= Bidirectional(GRU(12, input_shape=(938,6),return_sequences=True,return_state=False),merge_mode='concat')(x)
x = LeakyReLU(alpha=0.3)(x3)
x = Dropout(0.2)(x)
x = AttentionWithContext()(x)
x = BatchNormalization()(x)
x = LeakyReLU(alpha=0.3)(x)
x = Dropout(0.2)(x)
x = Dense(7,activation='sigmoid')(x)




                                                                                              #MODEL 4


x = Conv1D(12,kernel_size=3,strides=1, padding='same')(input)
x = LeakyReLU(alpha=0.3)(x)
x = Conv1D(12,kernel_size=3,strides=1, padding='same')(x)
x = LeakyReLU(alpha=0.3)(x)
x = Conv1D(12,kernel_size=24, strides = 2, padding='same')(x)
x = LeakyReLU(alpha=0.3)(x)
x = Dropout(0.2)(x)

x = Conv1D(12,kernel_size=3,strides=1, padding='same')(x)
x = LeakyReLU(alpha=0.3)(x)
x = Conv1D(12,kernel_size=3,strides=1, padding='same')(x)
x = LeakyReLU(alpha=0.3)(x)
x = Conv1D(12,kernel_size=24, strides = 2, padding='same')(x)
x = LeakyReLU(alpha=0.3)(x)
x = Dropout(0.2)(x)

x = Conv1D(12,kernel_size=3,strides=1, padding='same')(x)
x = LeakyReLU(alpha=0.3)(x)
x = Conv1D(12,kernel_size=3,strides=1, padding='same')(x)
x = LeakyReLU(alpha=0.3)(x)
x = Conv1D(12,kernel_size=24, strides = 2, padding='same')(x)
x = LeakyReLU(alpha=0.3)(x)
x = Dropout(0.2)(x) 

x = Conv1D(12,kernel_size=3,strides=1, padding='same')(x)
x = LeakyReLU(alpha=0.3)(x)
x = Conv1D(12,kernel_size=3,strides=1, padding='same')(x)
x = LeakyReLU(alpha=0.3)(x)
x = Conv1D(12,kernel_size=24, strides = 2, padding='same')(x)
x = LeakyReLU(alpha=0.3)(x)
x = Dropout(0.2)(x)

x = Conv1D(12,kernel_size=3,strides=1, padding='same')(x)
x = LeakyReLU(alpha=0.3)(x)
x = Conv1D(12,kernel_size=3,strides=1, padding='same')(x)
x = LeakyReLU(alpha=0.3)(x)
x = Conv1D(12,kernel_size=48, strides = 2, padding='same')(x)
x = LeakyReLU(alpha=0.3)(x)
x= Dropout(0.2)(x)
x4= Bidirectional(GRU(12, input_shape=(938,6),return_sequences=True,return_state=False),merge_mode='concat')(x)
x = LeakyReLU(alpha=0.3)(x4)
x = Dropout(0.2)(x)
x = AttentionWithContext()(x)
x = BatchNormalization()(x)
x = LeakyReLU(alpha=0.3)(x)
x = Dropout(0.2)(x)
x = Dense(7,activation='sigmoid')(x)


                                                                                  #MODEL 5



x = Conv1D(12,kernel_size=3,strides=1, padding='same')(input)
x = LeakyReLU(alpha=0.3)(x)
x = Conv1D(12,kernel_size=3,strides=1, padding='same')(x)
x = LeakyReLU(alpha=0.3)(x)
x = Conv1D(12,kernel_size=24, strides = 2, padding='same')(x)
x = LeakyReLU(alpha=0.3)(x)
x = Dropout(0.2)(x)

x = Conv1D(12,kernel_size=3,strides=1, padding='same')(x)
x = LeakyReLU(alpha=0.3)(x)
x = Conv1D(12,kernel_size=3,strides=1, padding='same')(x)
x = LeakyReLU(alpha=0.3)(x)
x = Conv1D(12,kernel_size=24, strides = 2, padding='same')(x)
x = LeakyReLU(alpha=0.3)(x)
x = Dropout(0.2)(x)

x = Conv1D(12,kernel_size=3,strides=1, padding='same')(x)
x = LeakyReLU(alpha=0.3)(x)
x = Conv1D(12,kernel_size=3,strides=1, padding='same')(x)
x = LeakyReLU(alpha=0.3)(x)
x = Conv1D(12,kernel_size=24, strides = 2, padding='same')(x)
x = LeakyReLU(alpha=0.3)(x)
x = Dropout(0.2)(x) 

x = Conv1D(12,kernel_size=3,strides=1, padding='same')(x)
x = LeakyReLU(alpha=0.3)(x)
x = Conv1D(12,kernel_size=3,strides=1, padding='same')(x)
x = LeakyReLU(alpha=0.3)(x)
x = Conv1D(12,kernel_size=24, strides = 2, padding='same')(x)
x = LeakyReLU(alpha=0.3)(x)
x = Dropout(0.2)(x)


x = Conv1D(12,kernel_size=3,strides=1, padding='same')(x)
x = LeakyReLU(alpha=0.3)(x)
x = Conv1D(12,kernel_size=3,strides=1, padding='same')(x)
x = LeakyReLU(alpha=0.3)(x)
x = Conv1D(12,kernel_size=48, strides = 2, padding='same')(x)
x = LeakyReLU(alpha=0.3)(x)
x = Dropout(0.2)(x)
x5= Bidirectional(GRU(12, input_shape=(938,6),return_sequences=True,return_state=False),merge_mode='concat')(x)
x = LeakyReLU(alpha=0.3)(x5)
x = Dropout(0.2)(x)
x = AttentionWithContext()(x)
x = BatchNormalization()(x)
x = LeakyReLU(alpha=0.3)(x)
x = Dropout(0.2)(x)
x= Dense(7,activation='sigmoid')(x)

  
       

                                                                                         #MODEL 6



x = Conv1D(12,kernel_size=3,strides=1, padding='same')(input)
x = LeakyReLU(alpha=0.3)(x)
x = Conv1D(12,kernel_size=3,strides=1, padding='same')(x)
x = LeakyReLU(alpha=0.3)(x)
x = Conv1D(12,kernel_size=24, strides = 2, padding='same')(x)
x = LeakyReLU(alpha=0.3)(x)
x = Dropout(0.2)(x)

x = Conv1D(12,kernel_size=3,strides=1, padding='same')(x)
x = LeakyReLU(alpha=0.3)(x)
x = Conv1D(12,kernel_size=3,strides=1, padding='same')(x)
x = LeakyReLU(alpha=0.3)(x)
x = Conv1D(12,kernel_size=24, strides = 2, padding='same')(x)
x = LeakyReLU(alpha=0.3)(x)
x = Dropout(0.2)(x)

x = Conv1D(12,kernel_size=3,strides=1, padding='same')(x)
x = LeakyReLU(alpha=0.3)(x)
x = Conv1D(12,kernel_size=3,strides=1, padding='same')(x)
x = LeakyReLU(alpha=0.3)(x)
x = Conv1D(12,kernel_size=24, strides = 2, padding='same')(x)
x = LeakyReLU(alpha=0.3)(x)
x = Dropout(0.2)(x) 

x = Conv1D(12,kernel_size=3,strides=1, padding='same')(x)
x = LeakyReLU(alpha=0.3)(x)
x = Conv1D(12,kernel_size=3,strides=1, padding='same')(x)
x = LeakyReLU(alpha=0.3)(x)
x = Conv1D(12,kernel_size=24, strides = 2, padding='same')(x)
x = LeakyReLU(alpha=0.3)(x)
x = Dropout(0.2)(x)

x = Conv1D(12,kernel_size=3,strides=1, padding='same')(x)
x = LeakyReLU(alpha=0.3)(x)
x = Conv1D(12,kernel_size=3,strides=1, padding='same')(x)
x = LeakyReLU(alpha=0.3)(x)
x = Conv1D(12,kernel_size=48, strides = 2, padding='same')(x)
x = LeakyReLU(alpha=0.3)(x)
x = Dropout(0.2)(x)
x6= Bidirectional(GRU(12, input_shape=(938,6),return_sequences=True,return_state=False),merge_mode='concat')(x)
x = LeakyReLU(alpha=0.3)(x6)
x = Dropout(0.2)(x)
x = AttentionWithContext()(x)
x = BatchNormalization()(x)
x = LeakyReLU(alpha=0.3)(x)
x = Dropout(0.2)(x)
x= Dense(7,activation='sigmoid')(x)

 #MERGE INPUT MODELS
z=concatenate([x1,x2,x3,x4,x5,x6])
print(z.shape)

#FINAL ATTENTIOON MODULE
x = AttentionWithContext()(z)
x = BatchNormalization()(x)
x = LeakyReLU(alpha=0.3)(x)
x = Dropout(0.2)(x)
x = Dense(50,activation='sigmoid')(x)
output = Dense(7,activation='sigmoid')(x)
model1 = Model(inputs=input,outputs=output)