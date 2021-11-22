const {
  colors,
  CssBaseline,
  ThemeProvider,
  Typography,
  Container,
  createTheme,
  Box,
  SvgIcon,
  Link,
  TextField,
  AppBar,
  Toolbar,
  IconButton,
  MenuIcon,
  Paper
} = MaterialUI;


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
    <Box sx={{ flexGrow: 1 }} style={{marginBottom: 40}}>
      <AppBar position="static">
        <Toolbar variant="dense">
          <Typography variant="h6" color="inherit" component="div">
            Levheim Cube Predictor
          </Typography>
        </Toolbar>
      </AppBar>
    </Box>
  );
}


function App() {
  const [value, setValue] = React.useState('Controlled');

  const handleChange = (event) => {
    setValue(event.target.value);
  };

  return (
    <div style={{background: "#cccc", height: '100vh'}}>
      <DenseAppBar/>
      <Box
      component="form"
      sx={{
        '& .MuiTextField-root': { m: 5, width: '80%' },
      }}
      noValidate
      autoComplete="off"
    >
      <div style={{maxWidth: 700, margin: '0 auto'}}>
        <Paper>
          <TextField
            id="standard-multiline-static"
            label="Enter the text (Only Russian is supported)"
            multiline
            rows={4}           
            variant="standard"
          />
          <TextField id="standard-basic" label="Enter code" variant="standard" />
        </Paper>        
      </div>
    </Box>
    </div>
  );
}

ReactDOM.render(
    <ThemeProvider theme={theme}>
      <CssBaseline />
      <App />
    </ThemeProvider>,
  document.querySelector('#root'),
);