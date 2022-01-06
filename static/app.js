const {
  colors,
  CssBaseline,
  ThemeProvider,
  Typography,
  Container,
  createTheme,
  Box,
  SvgIcon,
  TextField,
  AppBar,
  Toolbar,
  IconButton,
  MenuIcon,
  Menu,
  MenuItem,
  List,
  ListItem,
  ListItemText,
  Paper,
  Slider,
  Button,
  CircularProgress,
  Card,
  Avatar,
  Stack
} = MaterialUI;

const { Link, Route, HashRouter } = ReactRouterDOM;

const menuStyle = {
  display: 'flex',
  flexDirection: 'row',
  padding: 0,
  paddingLeft: 40
};

const headingStyle = {
  padding: 20
};

const centerImageStyle =  {
  width: '60%',
  display: 'block',
  margin: '0 auto'
}


// Create a theme instance.
const theme = createTheme({
  palette: {
    primary: {
      main: '#556cd6',
    },
    secondary: {
      main: '#19857b',
    },
    error: {
      main: colors.red.A400,
    },
  },
});

function DenseAppBar() {
  return (
    <Box sx={{ flexGrow: 1 }} style={{ marginBottom: 40 }}>
      <AppBar position="static">
        <Toolbar variant="dense">
          <Typography variant="h6" color="inherit" component="div">
            Levheim Cube Predictor
          </Typography>
          <List style={menuStyle}>
            <ListItem>
              <ListItemText><Link style={{ color: 'white', textDecoration: 'none' }} to="/app">App</Link></ListItemText>
            </ListItem>
            <ListItem>
              <ListItemText><Link style={{ color: 'white', textDecoration: 'none' }} to="/about">About</Link></ListItemText>
            </ListItem>
          </List>
        </Toolbar>
      </AppBar>
    </Box>
  );
}


function AboutPage() {
  return <Paper><div>
    <Card variant="outlined">
      <Typography style={headingStyle} variant="h4">About</Typography>
      <Typography style={{ padding: '20px' }} variant="body2" gutterBottom component="div">
      <img src='/images/cube1.jpg' style={centerImageStyle}></img>
       <p>This web application allows you to determine the emotional tonality of the Russian-language text. For that enter your text in the space and run the classifier by clicking the “analyze” button. As a result, the regressor will return you a prediction answer – a slider position on four scales of emotions. Thus, you can find out which emotions and to what extent (the position of the slider relative to the middle point of the scale) are represented in the text.</p>
       <p>The web application has been developed within a <b>project №. 19-012-00205 “Design of sentiment classifier for Internet-texts in Russian backed by Lövheim's Cube emotional model” supported by the Russian Foundation for Basic Research</b> and carried out by the researcher team of the Laboratory of Applied Linguistics and Cognitive Research (School of Philology and Language Communication) of the Siberian Federal University.</p>
       <p>In order to create the classifier a new method for a spatial emotional annotation of texts has been developed. It is based on the Lövheim Cube model of emotions and its main advantage is a possibility to situate the text in a multidimensional emotional space, thus, to receive complex and graduated emotional characteristics of the text. We have used a dataset with 3100 Internet texts in Russian, preselected according to thematic emotiogenic hashtags from the VKontakte social network. Our sample also includes neutral texts selected by a binary classifier. 2000 respondents participated in the emotional assessment of these texts on the crowdsourcing platform Yandex.Toloka. To create a classifier the transformer regression model DeepPavlov-RuBERT supplemented by a stack of fully connected layers has been applied </p>
      </Typography>
      <Button style={{display: 'block', margin: '0 auto', width: 130, textAlign: 'center', marginBottom: 20}} variant="contained" href="/#/app">Go to App</Button>
    </Card>

    <Card variant="outlined">
      <Typography style={headingStyle} variant="h4">Articles</Typography>
      <div style={{padding: 20}}>
        <ul>
          <li><a href="https://link.springer.com/chapter/10.1007/978-3-030-65218-0_12" target="_blank">Kolmogorova A., Kalinin A., Malikova A. (2020) Non-discrete Sentiment Dataset Annotation: Case Study for Lövheim Cube Emotional Model. </a></li>
          <li><a href="https://link.springer.com/chapter/10.1007/978-981-16-3742-1_17" target="_blank">Kolmogorova A., Kalinin A., Malikova A. (2021) Part-Whole Relation in Emotional Investigation of Verbal and Musical Text: Two Ways of Emotional Dataset Assessment. </a></li>
          <li><a href="http://ceur-ws.org/Vol-2852/paper6.pdf" target="_blank">Kolmogorova A.V., Kalinin A.A., Malikova A.V.(2020).The problem of retrieving neutral classes of texts in Russian in multiclass emotional text analysis. </a></li>
          <li><a href="https://link.springer.com/article/10.1007/s12304-021-09434-y" target="_blank">Kolmogorova A., Kalinin A., Malikova A. (2021) Semiotic Function of Empathy in Text Emotion Assessment.</a></li>
          <li><a href="https://www.europeanproceedings.com/article/10.15405/epsbs.2020.08.83" target="_blank">Kolmogorova A.V., Kalinin A.A., Malikova A.V. (2020) Syntactic Specificity of Texts Verbalizing Disgust and Shame</a></li>
        </ul>
      </div>
    </Card>

    <Card variant="outlined">
      <Typography style={headingStyle} variant="h4">Team</Typography>
      <div  style={{padding: 20}}>
      <List sx={{ width: '100%'}}>
        <ListItem alignItems="flex-start">
          <Avatar src='/images/Anastasia.jpg' sx={{ width: 100, height: 100 }}></Avatar>
          <ListItemText
            style={{paddingLeft: 20}}
            primary="Anastasiya Kolmogorova"
            secondary={
              <React.Fragment>
                <Typography
                  sx={{ display: 'inline' }}
                  component="span"
                  variant="body2"
                  color="text.primary"
                >
                  Research leader. Head of applied linguistics chair
                </Typography>
                <br/>
                <a href='mailto:nastiakol@mail.ru'>nastiakol@mail.ru</a>
            </React.Fragment>
          }
        />
        </ListItem>
        <ListItem alignItems="flex-start">
          <Avatar src='/images/foto_kalinin.png' sx={{ width: 100, height: 100 }}></Avatar>
          <ListItemText
            style={{paddingLeft: 20}}
            primary="Alexander Kalinin"
            secondary={
              <React.Fragment>
                <Typography
                  sx={{ display: 'inline' }}
                  component="span"
                  variant="body2"
                  color="text.primary"
                >
                  Lecturer. Developer
                </Typography>
            </React.Fragment>
          }
        />
        </ListItem>
        <ListItem alignItems="flex-start">
          <Avatar src='/images/alina.jpg' sx={{ width: 100, height: 100 }}></Avatar>
          <ListItemText
            style={{paddingLeft: 20}}
            primary="Alina Malikova"
            secondary={
              <React.Fragment>
                <Typography
                  sx={{ display: 'inline' }}
                  component="span"
                  variant="body2"
                  color="text.primary"
                >
                  Researcher. Lecturer
                </Typography>
            </React.Fragment>
          }
        />
        </ListItem>
        <ListItem alignItems="flex-start">
          <Avatar src='/images/Lyuba.jpg' sx={{ width: 100, height: 100 }}></Avatar>
          <ListItemText
            style={{paddingLeft: 20}}
            primary="Lyubov Kushko"
            secondary={
              <React.Fragment>
                <Typography
                  sx={{ display: 'inline' }}
                  component="span"
                  variant="body2"
                  color="text.primary"
                >
                  Researcher. Freelancer
                </Typography>
            </React.Fragment>
          }
        />
        </ListItem>
      </List>
      </div>
    </Card>
  </div>
  </Paper>;
}


function PredictPage() {
  const [text, setText] = React.useState('');
  const [code, setCode] = React.useState('');
  const [predictionsLoading, setLoading] = React.useState(false);

  const diagonalValues = ['shame_excitement', 'disgust_rage', 'fear_surprise', 'enjoyment_distress'];

  const initialState = diagonalValues.reduce((acc, entry) => ({ ...acc, [entry]: 0 }), {});

  const [sliderValues, setSliderValues] = React.useState(initialState);

  const marks = {
    'shame_excitement': [{ value: -5, label: 'Shame' }, { value: 0, label: '|' }, { value: 5, label: 'Excitement' }],
    'disgust_rage': [{ value: -5, label: 'Anger' }, { value: 0, label: '|' }, { value: 5, label: 'Disgust' }],
    'fear_surprise': [{ value: -5, label: 'Distress' }, { value: 0, label: '|' }, { value: 5, label: 'Enjoyment' }],
    'enjoyment_distress': [{ value: -5, label: 'Fear' }, { value: 0, label: '|' }, { value: 5, label: 'Surprise' }]
  }

  function valuetext(value) {
    return `${value}`;
  }

  function getPredictions() {
    setLoading(true);

    const requestOptions = {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ text: text, key: code })
    };

    fetch('/predict', requestOptions)
      .then(response => response.json())
      .then(response => setSliderValues(response))
      .finally(() => setLoading(false))
  }

  return <Paper>
    <TextField
      id="standard-multiline-static"
      label="Enter the text (Only Russian is supported)"
      multiline
      rows={10}
      variant="standard"
      value={text}
      onChange={(event) => setText(event.target.value)}
    />
    {predictionsLoading ?
      <div style={{ margin: '0 auto', textAlign: 'center' }}><CircularProgress /></div>
      :
      <div>
        <Button variant="contained" style={{ display: 'block', margin: '0 auto' }} onClick={getPredictions}>Analyze</Button>
        <div style={{ padding: 40 }}>
          {diagonalValues.map(diagonal =>
            <Slider
              key={diagonal}
              track={false}
              aria-labelledby="track-false-slider"
              value={sliderValues[diagonal]}
              getAriaValueText={valuetext}
              marks={marks[diagonal]}
              min={-5}
              max={5}
              disabled
            />
          )}
        </div>
      </div>
    }
  </Paper>
}


function App() {
  return (
    <HashRouter>
      <div style={{ background: "#cccc" }}>
        <DenseAppBar />
        <Box
          component="form"
          sx={{
            '& .MuiTextField-root': { m: 5, width: '80%' },
          }}
          noValidate
          autoComplete="off"
        >
          <div style={{ maxWidth: 700, margin: '0 auto' }}>
            <Route path="/" exact component={PredictPage} />
            <Route path="/app" component={PredictPage} />
            <Route path="/about" component={AboutPage} />
          </div>
        </Box>
      </div>

    </HashRouter>
  );
}

ReactDOM.render(
  <ThemeProvider theme={theme}>
    <CssBaseline />
    <App />
  </ThemeProvider>,
  document.querySelector('#root'),
);
