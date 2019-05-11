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

const Track = (props) => (
  <View style={{ marginTop: 10, marginBottom: 10, }}>
    <TouchableHighlight onPress={
      () => props.playTrack(props.track)
    }>
    <View>
      <View style={{ flexDirection: 'row', marginBottom: 5 }}>
        <Image
          style={{ width: 50, height: 50 }}
          source={{ uri: props.track.image, }}
          />
        <Text style={styles.track}>{props.track.title}</Text>
      </View>
      <Progress.Bar progress={props.track.percent} width={200} />
    </View>
    </TouchableHighlight>
  </View>
);

Track.propTypes = {
  track: PropTypes.object.isRequired,
  playTrack: PropTypes.func.isRequired,
};

const styles = StyleSheet.create({
  track: {
    padding: 10,
    fontSize: 18,
    height: 44,
  },
});

export default Track;
