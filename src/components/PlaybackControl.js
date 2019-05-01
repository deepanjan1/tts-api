import React from 'react';
import { StyleSheet, Text, View, Image } from 'react-native';
import * as Progress from 'react-native-progress';  // Progress bar
import PropTypes from 'prop-types';

const PlaybackControl = (props) => (
  <View style = { styles.container }>
    <Text>{ props.playTrack }</Text>
  </View>
);

PlaybackControl.propTypes = {
  playTrack: PropTypes.string.isRequired,
};

const styles = StyleSheet.create({
  container: {
    borderTopWidth: 1,
    padding: 10,
    fontSize: 18,
    height: 44,
  },
});

export default PlaybackControl;
