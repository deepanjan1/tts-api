import React from 'react';
import {
  StyleSheet,
  Text,
  View,
  Image,
  TouchableHighlight
} from 'react-native';
import * as Progress from 'react-native-progress';  // Progress bar

import Video from 'react-native-video';

import PropTypes from 'prop-types';

export default class PlaybackControl extends React.Component {
  constructor(props) {
    super(props);
  }

  state = {
    paused: true,
  };

  render = () => (
    <View style = { styles.container }>
      <Text>{ this.props.track.title }</Text>
      <Video
        source={{ uri: '366878130.mp3' }}
        ref={(ref) => {
          this.player = ref;
        }}

        paused={ this.state.paused }
        audioOnly={ true } />
      <TouchableHighlight onPress={ () => this.setState({ paused: false }) }>
        <View>
          <Image source={require('../assets/play_black.png')} />
        </View>
      </TouchableHighlight>
      <TouchableHighlight onPress={ () => this.setState({ paused: true }) }>
        <View>
          <Image source={require('../assets/pause_black.png')} />
        </View>
      </TouchableHighlight>
    </View>
  );
}

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
