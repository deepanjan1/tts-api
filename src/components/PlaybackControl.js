import React from 'react';
import {
  StyleSheet,
  Text,
  View,
  Image,
  TouchableHighlight
} from 'react-native';
import * as Progress from 'react-native-progress';  // Progress bar
import PropTypes from 'prop-types';

const PlaybackControl = (props) => (
  <View style = { styles.container }>
    <Text>{ props.track.title }</Text>
    <TouchableHighlight onPress={ () => console.log('play pressed') }>
      <View>
        <Image source={require('../assets/play_black.png')} />
      </View>
    </TouchableHighlight>
    <TouchableHighlight onPress={ () => console.log('pause pressed') }>
      <View>
        <Image source={require('../assets/pause_black.png')} />
      </View>
    </TouchableHighlight>
  </View>
);

PlaybackControl.propTypes = {
  track: PropTypes.object.isRequired,
};

const styles = StyleSheet.create({
  container: {
    borderTopWidth: 1,
    padding: 10,
    fontSize: 18,
    height: 44,
    flexDirection: 'row',
  },
});

export default PlaybackControl;
