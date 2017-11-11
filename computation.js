
'use strict';

module.exports = { // eslint-disable-line
  name: 'HI_dPCA',
  version: '0.0.1',
  cwd: __dirname,
  local: {
    type: 'cmd',
    cmd: 'python',
    args: ['./dpca_local.py'],
    verbose: true,
  },
  remote: {
    type: 'cmd',
    cmd: 'python',
    args: ['./dpca_master.py'],
    verbose: true,
  },
  plugins:['group-step'],
};
