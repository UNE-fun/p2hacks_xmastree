import React from 'react';
import './App.css';

interface AppProps {
}

interface AppState {
  timerID: number | null;
  date: string;
  treeimg_path: string;
}

class App extends React.Component<AppProps, AppState> {
  constructor(props: AppProps) {
    super(props);
    this.getTree = this.getTree.bind(this);
    this.changeDate = this.changeDate.bind(this);
    const now = new Date();
    this.state = {
      timerID: null,
      date: `${now.getFullYear()}-${(now.getMonth() + 1).toString().padStart(2, '0')}-${now.getDate().toString().padStart(2, '0')}`,
      treeimg_path: '',
    };
  }

  componentDidMount() {
    this.getTree();
  }

  async getTree() {
    console.log(this.state.date);
    const res = await fetch(`/tweets_at/${this.state.date}`);
    const treeimg_path = await res.text();
    this.setState({ treeimg_path });
  }

  changeDate(e: React.FormEvent<HTMLInputElement>) {
    if (this.state.timerID) window.clearTimeout(this.state.timerID);
    const timerID = window.setTimeout(this.getTree, 2000);
    this.setState({ timerID });
    const target = e.target as HTMLInputElement;
    this.setState({ date: target.value });
  }

  render() {
    return (
      <div className="App">
        <img src={`/static/media/${this.state.treeimg_path}`} />
        <input type="range" onChange={this.changeDate} />
      </div>
    );
  }
}

export default App;
