import React from 'react';
import {
  StyleSheet,
  Text,
  View,
} from 'react-native';
import { SafeAreaView } from 'react-navigation';
import { SearchBar } from 'react-native-elements';

export default class ArticleView extends React.Component {
  // adding a dummy state
  state = {
    search: '',
  };

  updateSearch = search => {
    this.setState({ search });
  };

  render () {
    const { search } = this.state;
    return (
      <View style={ styles.container }>
        <SafeAreaView style = {{ flex: 1 }}>
          <View style={ styles.headerContainer }>
            <Text>Home</Text>
          </View>
        </SafeAreaView>
        <View style={{ flex: 1, alignItems: 'stretch', flexDirection: 'column' }}>
          <SearchBar
            placeholder="Type Here..."
            onChangeText={this.updateSearch}
            value={search}
            Icon={ null }
            searchIcon={ null }
          />
        </View>
      </View>
    );
  }
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    justifyContent: 'center',
    alignItems: 'center',
    backgroundColor: '#F5FCFF',
  },
  headerContainer: {
    flex: 1,
  },
});
