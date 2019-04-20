import React from 'react';
import {
  StyleSheet,
  Text,
  View,
  FlatList,
  Image,
} from 'react-native';
import { SafeAreaView } from 'react-navigation'; // ensures title is below notch
import { SearchBar } from 'react-native-elements'; // Search bar

import Track from '../components/Track'; // Import track component

export default class ArticleView extends React.Component {
  // adding a dummy state
  state = {
    search: '',
    listData: [
      {
        key: 'Article 1',
        percent: 0.4,
        image: 'https://facebook.github.io/react-native/docs/assets/favicon.png',
      },
      {
        key: 'Article 2',
        percent: 0.4,
        image: 'https://facebook.github.io/react-native/docs/assets/favicon.png',
      },
      {
        key: 'Article 3',
        percent: 0.4,
        image: 'https://facebook.github.io/react-native/docs/assets/favicon.png',
      },
      {
        key: 'Article 4',
        percent: 0.4,
        image: 'https://facebook.github.io/react-native/docs/assets/favicon.png',
      },
      {
        key: 'Article 5',
        percent: 0.4,
        image: 'https://facebook.github.io/react-native/docs/assets/favicon.png',
      },
      {
        key: 'Article 6',
        percent: 0.4,
        image: 'https://facebook.github.io/react-native/docs/assets/favicon.png',
      },
      {
        key: 'Article 7',
        percent: 0.4,
        image: 'https://facebook.github.io/react-native/docs/assets/favicon.png',
      },
      {
        key: 'Article 8',
        percent: 0.7,
        image: 'https://facebook.github.io/react-native/docs/assets/favicon.png',
      },
      {
        key: 'Article 9',
        percent: 0.7,
        image: 'https://facebook.github.io/react-native/docs/assets/favicon.png',
      },
    ],
  };

  updateSearch = search => {
    this.setState({ search });
  };

  render () {
    const { search } = this.state;
    return (
      <View style={ styles.container }>
        <SafeAreaView>
          <Text style={{ textAlign: 'center', marginBottom: 5, }}>Home</Text>
        </SafeAreaView>
        <View>
          <SearchBar
            placeholder="Type Here..."
            onChangeText={this.updateSearch}
            value={search}
            Icon={ null }
            searchIcon={ null }
          />
        </View>
        <View style={ styles.horizontalRule } />
        <FlatList
          data={ this.state.listData }
          renderItem={({ item }) =>
            <Track track = { item } />
          }
        />
      </View>
    );
  }
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    justifyContent: 'flex-start',
    alignItems: 'stretch',
    backgroundColor: '#F5FCFF',
    marginRight: 5,
    marginLeft: 5,
  },
  horizontalRule: {
    marginTop: 5,
    marginBottom: 5,
    borderBottomColor: 'black',
    borderBottomWidth: 1,
  },
});
