# this program trains to predict MNIST up to 92% accuracy

from tensorflow.examples.tutorials.mnist import input_data
mnist = input_data.read_data_sets("MNIST_data/", one_hot=True)

pass

import tensorflow as tf
x = tf.placeholder(tf.float32, [None, 784])


W = tf.Variable(tf.zeros([784, 10]))
b = tf.Variable(tf.zeros([10]))

y = tf.nn.softmax(tf.matmul(x, W) + b)

y_ = tf.placeholder(tf.float32, [None, 10])

cross_entropy = tf.reduce_mean(-tf.reduce_sum(y_ * tf.log(y), reduction_indices=[1]))

train_step = tf.train.GradientDescentOptimizer(0.1).minimize(cross_entropy)

sess = tf.InteractiveSession()

tf.global_variables_initializer().run()

correct_prediction = tf.equal(tf.argmax(y,1), tf.argmax(y_,1))

accuracy = tf.reduce_mean(tf.cast(correct_prediction, tf.float32))

for epoch in range(1000):
    for _ in range(100):
        batch_xs, batch_ys = mnist.train.next_batch(500)
        sess.run(train_step, feed_dict={x: batch_xs, y_: batch_ys})

    print("epoch: ", epoch, "    accuracy: ", sess.run(accuracy, feed_dict={x: mnist.test.images, y_: mnist.test.labels}))


