import { Routes } from '@angular/router';
import { MainModule } from './main/main-module';

export const routes: Routes = [
  {
    path: '',
    loadChildren: () => import('./main/main-module').then((m) => m.MainModule),
  },
];
