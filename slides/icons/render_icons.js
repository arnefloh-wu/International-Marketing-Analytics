// Render Lucide line icons to PNG in the WU navy (tx2) and white, 256 px.
const React = require('react'); const { renderToStaticMarkup } = require('react-dom/server');
const sharp = require('sharp'); const lu = require('react-icons/lu'); const path = require('path');
const OUT = process.argv[2];
const names = ['LuChartLine','LuEuro','LuGlobe','LuCandy','LuBot','LuScale','LuSplit','LuFlaskConical','LuCode','LuMessagesSquare',
  'LuSchool','LuHouse','LuClock','LuFileText','LuFileSpreadsheet','LuPresentation','LuNotebookPen','LuGraduationCap','LuGitBranch',
  'LuLaptop','LuListChecks','LuClipboardCheck','LuShieldCheck','LuUsers','LuLightbulb','LuTarget','LuMic','LuPencilLine','LuBriefcase','LuFlag','LuSparkles','LuBookOpen'];
(async () => {
  for (const n of names) {
    for (const [tag, color] of [['navy', '#002350'], ['white', '#FFFFFF'], ['blue', '#0096D3']]) {
      const svg = renderToStaticMarkup(React.createElement(lu[n], { size: 256, color, strokeWidth: 1.75 }));
      await sharp(Buffer.from(svg)).resize(256, 256).png().toFile(path.join(OUT, `${n}-${tag}.png`));
    }
  }
  console.log('rendered', names.length * 3);
})();
