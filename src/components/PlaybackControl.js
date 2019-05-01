import React from 'react';
import { StyleSheet, Text, View, Image } from 'react-native';
import * as Progress from 'react-native-progress';  // Progress bar
import PropTypes from 'prop-types';

const PlaybackControls = () => (
  <View style = { styles.container }>
    <Text>Not Playing Anything</Text>
  </View>
);

// PlaybackControls.propTypes = {
//
// };

const styles = StyleSheet.create({
  container: {
    borderTopWidth: 1,
    padding: 10,
    fontSize: 18,
    height: 44,
  },
});

export default PlaybackControls;
