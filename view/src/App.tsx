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
      date: now.toISOString(),
      treeimg_path: '',
   };
  }

  async componentDidMount() {
    this.getTree();
  }

  async getTree() {
    const date_str = this.state.date.replace(/\.\d+Z$/, '');
    const res = await fetch(`/tweets_at/${date_str}`);
    const treeimg_path = await res.text();
    this.setState({ treeimg_path });
  }

  changeDate(e: React.FormEvent<HTMLInputElement>) {
    if (this.state.timerID) window.clearTimeout(this.state.timerID);
    const timerID = window.setTimeout(this.getTree, 2000);
    this.setState({ timerID });
    const target = e.target as HTMLInputElement;
    const now = new Date();
    now.setMinutes(Math.floor(now.getMinutes() / 15) * 15 + Number(target.value) * 15);
    this.setState({ date: now.toISOString() });
  }

  render() {
    return (
      <div className="App">
        <div>{ this.state.date }</div>
        <input type="range" onChange={this.changeDate} max="0" min="-50" />
        <div>
          <img src={`/static/media/${this.state.treeimg_path}`} className="treeimg" />
        </div>
      </div>
    );
  }
}

export default App;
