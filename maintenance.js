/* Set to true to enable maintenance mode site-wide. */
const MAINTENANCE_MODE = false;
const MAINTENANCE_PAGE = 'maintenance.html';
if(MAINTENANCE_MODE && !location.pathname.endsWith(MAINTENANCE_PAGE)){location.replace(MAINTENANCE_PAGE)}
